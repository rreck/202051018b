```json
{
  "id": "cc3b4e4bf23afd8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293241,
  "host_pid": "9e6742732c60:1",
  "hash": "6c11a07dae1b6bf8d388115e7b4eed79afb0b4850210f9fed344e8beccc8644f",
  "cid": "QmV16c11a07dae1b6bf8d388115e7b4eed79afb0b485",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293241,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293241
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "48db6bab4a1d903391ee9bcee734c0bec7a9af9c5bb6572a20c1ae308f607c57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 106623788, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}
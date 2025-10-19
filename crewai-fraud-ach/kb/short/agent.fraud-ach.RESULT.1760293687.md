```json
{
  "id": "33cbd37bb26bcf0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293687,
  "host_pid": "9e6742732c60:1",
  "hash": "15cce1f943aaf3222a0da62c348c513e46b126acf6ac81a91a8f377ad2bd8fd4",
  "cid": "QmV115cce1f943aaf3222a0da62c348c513e46b126ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293687,
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
      "evaluated_at": 1760293687
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
  "sig": "c4f2772d5179876dd20e7cbddbc76aec6abbd1217d69c1a2e500368dfafab5df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153543170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 21357825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}
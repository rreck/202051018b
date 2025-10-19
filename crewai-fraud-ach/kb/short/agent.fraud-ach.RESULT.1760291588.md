```json
{
  "id": "bb06ffd581ed9b61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291588,
  "host_pid": "9e6742732c60:1",
  "hash": "47cd87037b5f64c0cca39230777dbf6103f27e34837cf18393ae99be535d59b8",
  "cid": "QmV147cd87037b5f64c0cca39230777dbf6103f27e34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291588,
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
      "evaluated_at": 1760291588
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
  "sig": "88865f2df1b3d9da764e6bc1c24e051e0993959d71a975c879a5f8f70cf81de3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 65511832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}
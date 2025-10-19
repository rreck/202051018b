```json
{
  "id": "87af3c184db958b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291665,
  "host_pid": "9e6742732c60:1",
  "hash": "9898fad541b5c935dfd57cc4b4a7f24bb66ec10e3fa8bd455d129c4fabe55a89",
  "cid": "QmV19898fad541b5c935dfd57cc4b4a7f24bb66ec10e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291665,
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
      "evaluated_at": 1760291665
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
  "sig": "6764d4b19f70fa335595b375e248470139f0f51901e4ce36ec44401a542184ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596690593
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 256, 'threshold': 50, 'total_amount': 36084480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 255, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}
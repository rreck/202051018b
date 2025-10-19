```json
{
  "id": "3c5438e233f9a668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292428,
  "host_pid": "9e6742732c60:1",
  "hash": "dc216f3317a623480e7a2ca28fcd39ec7503cf64d6c20cb0489b637a4636b9d6",
  "cid": "QmV1dc216f3317a623480e7a2ca28fcd39ec7503cf64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292428,
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
      "evaluated_at": 1760292428
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
  "sig": "0774775a60535a2cef411156109c2e075d74566807180b7767f6e0c50807de18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242987850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 23054713, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}
```json
{
  "id": "d924f2a92cb4889d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291408,
  "host_pid": "9e6742732c60:1",
  "hash": "2be2395be81462da2393caf507a3c7d9fc12244937b10ad3d3c793da9d724c3f",
  "cid": "QmV12be2395be81462da2393caf507a3c7d9fc122449",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291408,
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
      "evaluated_at": 1760291408
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
  "sig": "3ed0c78a8da4f8f0dcf56e7a6a919d270b975eb057a7633c57f42ce65a6ba0ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 23528106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}
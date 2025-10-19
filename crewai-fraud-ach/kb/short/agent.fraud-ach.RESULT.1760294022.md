```json
{
  "id": "230973fde4c13ecc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294022,
  "host_pid": "9e6742732c60:1",
  "hash": "6869963602b2b8c3030b8b003e4efceaacf9e5086d02b04dd7addbe969f99ff9",
  "cid": "QmV16869963602b2b8c3030b8b003e4efceaacf9e508",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294022,
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
      "evaluated_at": 1760294022
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
  "sig": "dcb73a440706daa516dcae3cab7d9778749392bd97102998254c766e6b3f4f52"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 93613450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}
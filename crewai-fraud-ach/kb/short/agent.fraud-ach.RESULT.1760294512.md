```json
{
  "id": "ea728d79f22f608c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294512,
  "host_pid": "9e6742732c60:1",
  "hash": "733be392fe05860d2d4ad19a9743109cf82c6d86b63a12f2c74175300798a548",
  "cid": "QmV1733be392fe05860d2d4ad19a9743109cf82c6d86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294512,
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
      "evaluated_at": 1760294512
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
  "sig": "0206477549b57173700792ffe3c45f15d2d1f8479a55b16891fc6a9836254303"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151102645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 98237126, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '9dd268c0fa996698'}}}
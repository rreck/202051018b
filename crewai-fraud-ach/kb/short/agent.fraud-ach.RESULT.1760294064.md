```json
{
  "id": "f479484baf823869",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294064,
  "host_pid": "9e6742732c60:1",
  "hash": "124369a5917a97833344a0c36f2eb17966fb9616658baa923011ed6688195baf",
  "cid": "QmV1124369a5917a97833344a0c36f2eb17966fb9616",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294064,
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
      "evaluated_at": 1760294064
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
  "sig": "0d8e77cf465e36c7551c6fb1dbd073014ff80fb72fd451ce3c5309daf85cd90c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153452209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 72807966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': 'ba46400915da6233'}}}
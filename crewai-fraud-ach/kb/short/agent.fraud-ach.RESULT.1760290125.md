```json
{
  "id": "6275bf37b36f4d24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290125,
  "host_pid": "9e6742732c60:1",
  "hash": "648938b24708f19334c48530a462de709ec61f4a64379153bdf39b44401b9a24",
  "cid": "QmV1648938b24708f19334c48530a462de709ec61f4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290125,
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
      "evaluated_at": 1760290125
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
  "sig": "8e8ff01af6b9df3172eb3371e289ad688ae30f1c9b50633a9bce2332b3f27f61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593769639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 60953216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'cb8c3421a3879068'}}}
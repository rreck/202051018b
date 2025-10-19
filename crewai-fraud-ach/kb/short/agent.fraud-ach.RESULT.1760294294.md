```json
{
  "id": "9fcf700d6101ffff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294294,
  "host_pid": "9e6742732c60:1",
  "hash": "19d1e9839dedf2adee6fb83bac87d6556cb726bc177771adef177b54d6e8a6a4",
  "cid": "QmV119d1e9839dedf2adee6fb83bac87d6556cb726bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294294,
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
      "evaluated_at": 1760294294
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
  "sig": "b1d204695d0f9df226a0e0a0b399b44519aad9394dd2bf62ae20a1feef755b79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594679703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 21553730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': 'e094f64527cf9b58'}}}
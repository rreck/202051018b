```json
{
  "id": "dcca7b7e81aa76ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293863,
  "host_pid": "9e6742732c60:1",
  "hash": "e0ae49d6cc059e756556a55140f2245a16dadfd6c1640345162e7bc239d98f68",
  "cid": "QmV1e0ae49d6cc059e756556a55140f2245a16dadfd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293863,
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
      "evaluated_at": 1760293863
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
  "sig": "732d31b17b89eb43e0672b9e2b445586bf3c497ad801885c92b3f1c16dc2b9b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244807015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 22700000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': 'e3fbbc71f2accf8f'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}
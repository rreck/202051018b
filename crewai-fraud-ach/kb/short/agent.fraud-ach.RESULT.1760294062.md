```json
{
  "id": "19a78379e4de304a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294062,
  "host_pid": "9e6742732c60:1",
  "hash": "605655d553e9261e2e3dd0ae1dc99d91c569895da84868ed75db34aaff1e7eec",
  "cid": "QmV1605655d553e9261e2e3dd0ae1dc99d91c569895d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294062,
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
      "evaluated_at": 1760294062
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
  "sig": "62fc0dfd78fe96458e0737a4e603f931b867196ef2dc0dc9ca3177ff42653e49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037116719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 41149416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': 'c24831f619c6556e'}}}
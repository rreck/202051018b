```json
{
  "id": "6fc3b94cd82eb094",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294701,
  "host_pid": "9e6742732c60:1",
  "hash": "605590f38ebf4f62c1811a9ebe95dec2461f0c084ce1e60f15aff36a74b1116e",
  "cid": "QmV1605590f38ebf4f62c1811a9ebe95dec2461f0c08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294701,
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
      "evaluated_at": 1760294701
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
  "sig": "d2d02c6ce6ea2bb56c5904f2ab9f3e327c1724a2fe07814c1204860cdf2542e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464280863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 33803973, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '89fc487441475897'}}}}
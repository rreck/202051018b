```json
{
  "id": "ac980f566280d578",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293130,
  "host_pid": "9e6742732c60:1",
  "hash": "5ff0afb503e28d42fb56c7d57d14cddfa4140b7137a62971dec289817eb020bd",
  "cid": "QmV15ff0afb503e28d42fb56c7d57d14cddfa4140b71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293130,
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
      "evaluated_at": 1760293130
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
  "sig": "f7764b3e1b90ccb5afa9e1bf24268ea54c98a14e9df7cafb499962224199b77d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 103645104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}
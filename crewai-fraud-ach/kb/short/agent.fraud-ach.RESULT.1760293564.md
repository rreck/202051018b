```json
{
  "id": "0c72da8d9e8dfd00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293564,
  "host_pid": "9e6742732c60:1",
  "hash": "31277bc4ab0a30312f490077fbb9744d84c6206554b94d15a09e0d4b6cc090b4",
  "cid": "QmV131277bc4ab0a30312f490077fbb9744d84c62065",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293564,
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
      "evaluated_at": 1760293564
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
  "sig": "00244258d353930dcd3d82e05e0bced7450528f3153c3f9ecbf82a0dd7e4f99e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156823921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 61775025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '5764ccd6c01b314b'}}}maly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6602570}}}
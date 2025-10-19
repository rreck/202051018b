```json
{
  "id": "dfa0250ca952d690",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293309,
  "host_pid": "9e6742732c60:1",
  "hash": "e9aeaf90fe95f6a62c9f7da97368037ddb2204d0902b466afa858c603540b6a0",
  "cid": "QmV1e9aeaf90fe95f6a62c9f7da97368037ddb2204d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293309,
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
      "evaluated_at": 1760293309
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
  "sig": "960c352b483a973e7e78bc4ee919bb857cdce8627328720dc137b599deb678f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 82383696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}maly': {'fraud_detected': True, 'risk_score': 87, 'details': {'zscore': 4.79, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9144651}}}
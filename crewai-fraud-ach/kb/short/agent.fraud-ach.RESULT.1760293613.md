```json
{
  "id": "bb167771b381d634",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293613,
  "host_pid": "9e6742732c60:1",
  "hash": "015dd1f793d3d9a98a1730473569eefccebaab98973cdc93c323cafd3c0d314b",
  "cid": "QmV1015dd1f793d3d9a98a1730473569eefccebaab98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293613,
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
      "evaluated_at": 1760293613
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
  "sig": "a1d9af4b7e310244f6cc5024ebe2f65a7f3d818707144dd3bbc6cab9ed077d2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592248809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 38513448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'ed3ae9155c1e3edb'}}}
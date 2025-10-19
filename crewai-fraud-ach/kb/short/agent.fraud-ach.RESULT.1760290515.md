```json
{
  "id": "0a3f665f59d2763c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290515,
  "host_pid": "9e6742732c60:1",
  "hash": "243172131873dad9c077fff5bcfb55f8ae1fe3c02432a3173627cc99f382639d",
  "cid": "QmV1243172131873dad9c077fff5bcfb55f8ae1fe3c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290515,
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
      "evaluated_at": 1760290515
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
  "sig": "09661f18953222e8bbb94bea274eb282fe6b95a2dedf31ebea0bbfbb3567dacf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 34767568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'c5ade7cea17f41fa'}}}
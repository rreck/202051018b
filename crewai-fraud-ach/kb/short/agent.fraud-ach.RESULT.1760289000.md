```json
{
  "id": "38e956caddcaa846",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289000,
  "host_pid": "9e6742732c60:1",
  "hash": "ca9a222c3d3620a687de6df6879be98ce93bb2bd301c94d9b2dc64eb6a406ee4",
  "cid": "QmV1ca9a222c3d3620a687de6df6879be98ce93bb2bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289000,
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
      "evaluated_at": 1760289000
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
  "sig": "2d2316d5344fe5eaebec8d23ce670191b970003e6da1627f13d3657b2afbdde8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 36787080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}
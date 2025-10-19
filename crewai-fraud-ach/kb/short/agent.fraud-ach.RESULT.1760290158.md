```json
{
  "id": "55a682f2f8cb71e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290158,
  "host_pid": "9e6742732c60:1",
  "hash": "8202959f2e3ad59852867face42346cf58a0bc38de005241960139f2143fd617",
  "cid": "QmV18202959f2e3ad59852867face42346cf58a0bc38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290158,
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
      "evaluated_at": 1760290158
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
  "sig": "add2b406b8884a7126cc0f48b82b3eeed8f7bed84fdf21dd1835c4af8c9fae0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462772191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 29287687, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '3cc4f4a3442921e3'}}}
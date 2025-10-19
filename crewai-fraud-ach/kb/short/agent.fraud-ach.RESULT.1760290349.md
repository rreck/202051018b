```json
{
  "id": "2001bd26219a63c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290349,
  "host_pid": "9e6742732c60:1",
  "hash": "f1a77121f869fb75735dca196afc90864d0db65352e9721f78450f5c231d9f32",
  "cid": "QmV1f1a77121f869fb75735dca196afc90864d0db653",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290349,
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
      "evaluated_at": 1760290349
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
  "sig": "d2b52a864245200a8618e5a85b9e63ca835ecce7196541b80107db63012cf7ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 40870200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}
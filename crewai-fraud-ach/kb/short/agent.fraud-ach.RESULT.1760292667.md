```json
{
  "id": "a8732a06835b8a69",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292667,
  "host_pid": "9e6742732c60:1",
  "hash": "d90dbe4d2b2e81de6b914ecc5e333168f17703ec98d5ad33468448da99887263",
  "cid": "QmV1d90dbe4d2b2e81de6b914ecc5e333168f17703ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292667,
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
      "evaluated_at": 1760292667
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "737ac1c2097621ba844b0708100428958a872500eb521bc78a58547bf3545186"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 62809072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}
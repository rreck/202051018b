```json
{
  "id": "33b26918ba53d537",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292334,
  "host_pid": "9e6742732c60:1",
  "hash": "2530deae56ee113e2f8d1aef097616fd3372d05e7885196ff21bcec7197e6e7a",
  "cid": "QmV12530deae56ee113e2f8d1aef097616fd3372d05e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292334,
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
      "evaluated_at": 1760292334
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
  "sig": "341d32ed930c4a3412e497d72aa30a42cdb07966ee2028c1ab615d0241dc7acb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 12907050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}
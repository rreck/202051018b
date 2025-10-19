```json
{
  "id": "71b13e153b8ff3bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290789,
  "host_pid": "9e6742732c60:1",
  "hash": "a81e448fbb972869e8b5518a237b907e8b97da3d69289ba3da81deaca1d89133",
  "cid": "QmV1a81e448fbb972869e8b5518a237b907e8b97da3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290789,
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
      "evaluated_at": 1760290789
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
  "sig": "d5ae1a2fd18ae2612b3423f489d2c52622cbea986348367782210fd9f9c58722"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279970164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 29359668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}
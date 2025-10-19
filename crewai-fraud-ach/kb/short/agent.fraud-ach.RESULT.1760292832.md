```json
{
  "id": "d74f64a25088dd24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292832,
  "host_pid": "9e6742732c60:1",
  "hash": "25a6f9cb5bd4225a19e874d6ab9fd1d4c5a6c5778f87224868cf5116fb201cbd",
  "cid": "QmV125a6f9cb5bd4225a19e874d6ab9fd1d4c5a6c577",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292832,
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
      "evaluated_at": 1760292832
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
  "sig": "41d96f2a241999f58e3d9a21e419e2b21039d5de591a8c11ca530bf8c3f8180a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 33312672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}
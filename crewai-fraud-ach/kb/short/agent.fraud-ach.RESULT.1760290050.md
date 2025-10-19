```json
{
  "id": "4b362293cd165135",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290050,
  "host_pid": "9e6742732c60:1",
  "hash": "53f4cbac2d5dfdbdd2850370d6169ccee6f46e928402682aa088f72681925715",
  "cid": "QmV153f4cbac2d5dfdbdd2850370d6169ccee6f46e92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290050,
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
      "evaluated_at": 1760290050
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
  "sig": "799e76384fc1ae2cd170fe29fc4f649c2cc02e38e87468841b8749ee0564babd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272098114
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 58023140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285764, 'matching_hash': '010bb0d7cfc5cc6e'}}}
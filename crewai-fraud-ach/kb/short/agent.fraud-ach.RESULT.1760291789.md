```json
{
  "id": "f82a39310084550b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291789,
  "host_pid": "9e6742732c60:1",
  "hash": "2a51d05045ca97889b4a15f389ec8542b61d0b08c89740ba9a65bd45e0e8341d",
  "cid": "QmV12a51d05045ca97889b4a15f389ec8542b61d0b08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291789,
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
      "evaluated_at": 1760291789
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
  "sig": "8542bbfd979a864e924a612243c48b82fea472cfae81eabac541463d753c7485"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272525723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 16775976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '7f6b158faad48b99'}}}
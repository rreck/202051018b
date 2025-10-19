```json
{
  "id": "c3547f22e9b33149",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293386,
  "host_pid": "9e6742732c60:1",
  "hash": "69c865dfe9730ef2b51e60ac11e22399f5d2e2b4f471e83faa4115f4db6344bb",
  "cid": "QmV169c865dfe9730ef2b51e60ac11e22399f5d2e2b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293386,
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
      "evaluated_at": 1760293386
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
  "sig": "d86f6efd023612d642f34af5374292ed46059c77c7060f30298a3d45ce895d60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 24603026, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}
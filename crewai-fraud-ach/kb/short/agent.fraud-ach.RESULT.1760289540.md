```json
{
  "id": "6f60dcf914a3e0d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289540,
  "host_pid": "9e6742732c60:1",
  "hash": "2afe7615428648b9b03df62086fd00d007252f205e3edfb38ba9c3b335c1a904",
  "cid": "QmV12afe7615428648b9b03df62086fd00d007252f20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289540,
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
      "evaluated_at": 1760289540
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
  "sig": "ba5c3aea0ff7a8ac0813936e350af9de3de6cd2b91521a0d5c6f2d5ab570ef1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462495850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 32996502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '1976ee1fa1c7bc70'}}}
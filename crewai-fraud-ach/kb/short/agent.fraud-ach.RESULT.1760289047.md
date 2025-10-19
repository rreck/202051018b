```json
{
  "id": "1a23896d7b8009a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289047,
  "host_pid": "9e6742732c60:1",
  "hash": "04bab903e6978f184151ca3452dc66f08137223d5d92ab9b925606830c44b1fa",
  "cid": "QmV104bab903e6978f184151ca3452dc66f08137223d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289047,
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
      "evaluated_at": 1760289047
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
  "sig": "23fb922ccaba62dcd5233ab23ac3086a71d3275a42b363028654a2dff014ac61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278201542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 32963280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': 'ee525b8c336c7bb1'}}}
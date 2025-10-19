```json
{
  "id": "9933b60aae38f319",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291335,
  "host_pid": "9e6742732c60:1",
  "hash": "4de8759596e1175a3969078dd713bace28e441b71452f33589dcaa3335a7460a",
  "cid": "QmV14de8759596e1175a3969078dd713bace28e441b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291335,
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
      "evaluated_at": 1760291335
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
  "sig": "9fa1377512a77611b68ba28750544d216da70e98b78fd09f977be77e8545e3d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024542500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 74537576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}
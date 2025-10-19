```json
{
  "id": "34cd48f43c8d2d7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290290,
  "host_pid": "9e6742732c60:1",
  "hash": "730a208df0fc55135a2eec2be11b26febdbda2a7a8188a4342cb440ad851c810",
  "cid": "QmV1730a208df0fc55135a2eec2be11b26febdbda2a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290290,
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
      "evaluated_at": 1760290290
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
  "sig": "899a1d73926f61220e16d57ead91130dc83edd437eb981066abcc219407fe473"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593122933
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 59074374, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '1a44b34bf830cda9'}}}
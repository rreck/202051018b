```json
{
  "id": "1c731ea3d839fe79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291868,
  "host_pid": "9e6742732c60:1",
  "hash": "5841ab4a0e0c1fa5acc875de3e25a30b603879a475720e4254916f5507b7aac8",
  "cid": "QmV15841ab4a0e0c1fa5acc875de3e25a30b603879a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291868,
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
      "evaluated_at": 1760291868
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
  "sig": "cbaccded5f8295f745bef3c4cd6e748c31a1910af02dc82b53ea2e0c904ef4a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026044300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 71097905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '19d391c08a2c00ab'}}}
```json
{
  "id": "31e8d8ab14e46e46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289056,
  "host_pid": "9e6742732c60:1",
  "hash": "892a8bb5bf327e85e5387dc753ec3ca3c773fe4c472d1658a260cddd888c1326",
  "cid": "QmV1892a8bb5bf327e85e5387dc753ec3ca3c773fe4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289056,
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
      "evaluated_at": 1760289056
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
  "sig": "c689e3732442fd35c653bd80ec11078340b674f8c69117feabb2436a1725b4ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 50659280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}
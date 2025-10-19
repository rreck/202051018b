```json
{
  "id": "2f1dbffe78b63f5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289568,
  "host_pid": "9e6742732c60:1",
  "hash": "75525248d35e161d2918d6c67bb60c34663a78bc7c0df36e7aa3d2f03e32ae0a",
  "cid": "QmV175525248d35e161d2918d6c67bb60c34663a78bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289568,
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
      "evaluated_at": 1760289568
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
  "sig": "c2702cb9d3b60106deb64c42f77dab2cb0f00d7618c83ebf06d12f1653a59d00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 16957929, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}
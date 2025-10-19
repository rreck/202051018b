```json
{
  "id": "e9b18f7b4d69c968",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293219,
  "host_pid": "9e6742732c60:1",
  "hash": "887c96624910518e40adeabaeb32aafbc2eeeb2d26f104b3a3f3ee0c87ffcbaa",
  "cid": "QmV1887c96624910518e40adeabaeb32aafbc2eeeb2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293219,
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
      "evaluated_at": 1760293219
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
  "sig": "8173eb17d8bba75add621b67a22ac7938dcdf81d50d40222b3d2840f441c77c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463583993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 74461942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '335771e11ddee318'}}}
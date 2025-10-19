```json
{
  "id": "9735386b7da0e1ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291692,
  "host_pid": "9e6742732c60:1",
  "hash": "5598dc0d669eb6cd36b283537a0c7e55eea7c2ff53916aa60474fb1868d6dd84",
  "cid": "QmV15598dc0d669eb6cd36b283537a0c7e55eea7c2ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291692,
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
      "evaluated_at": 1760291692
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
  "sig": "5be0ae8bb5ebce93cdb56a81cf1400d5b549f4fa8e92adb7dea4f6373d23c14b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469776996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 29738300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '22919e1176d7109e'}}}
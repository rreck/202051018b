```json
{
  "id": "d359ae2a73004aed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290062,
  "host_pid": "9e6742732c60:1",
  "hash": "73a81784b8b35478c2a49928d42be2194213443f81b952d6de47209363e795c0",
  "cid": "QmV173a81784b8b35478c2a49928d42be2194213443f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290062,
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
      "evaluated_at": 1760290062
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
  "sig": "fb307912072a66c0a490a594dfb05cfa64cb8bc354537576ec50bd25a04f9ce6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021597485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 37777880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': '53d96e948794c738'}}}
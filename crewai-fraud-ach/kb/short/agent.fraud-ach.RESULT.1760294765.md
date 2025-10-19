```json
{
  "id": "6ea0d7d86583dce5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294765,
  "host_pid": "9e6742732c60:1",
  "hash": "5ea3ee60e2761347edae67140127c75e739b40063fdc1e9a34b6b58ede6ee3a4",
  "cid": "QmV15ea3ee60e2761347edae67140127c75e739b4006",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294765,
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
      "evaluated_at": 1760294765
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
  "sig": "a35169f6192431897f2dea61efb86819ff03d8f7a495fed5a61858c2e3f2fe60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595764750
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 23134372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '81dd493231a1d242'}}}
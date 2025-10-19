```json
{
  "id": "a6c0e2f7d6af5e18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291226,
  "host_pid": "9e6742732c60:1",
  "hash": "5665d73e3a96b058e5cfeaf3fa15939cca96fa3ccf90b24130091bdfec92f46f",
  "cid": "QmV15665d73e3a96b058e5cfeaf3fa15939cca96fa3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291226,
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
      "evaluated_at": 1760291226
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
  "sig": "e3805ed0e6145e5c00999e80a820a1a54d1a355c4de168a19d21defb5eea9365"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245652457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 14456290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '6ac12dd8f1799493'}}}
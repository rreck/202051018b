```json
{
  "id": "af6586d59758c79e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294255,
  "host_pid": "9e6742732c60:1",
  "hash": "4367c7cb5b64eb712d551747e8d2e5a93c058e1c8a6ce86a299a570083c438e5",
  "cid": "QmV14367c7cb5b64eb712d551747e8d2e5a93c058e1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294255,
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
      "evaluated_at": 1760294255
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
  "sig": "7fc5201bfd564d985ec8afdda6a6712830c16a7082f502acf3085e15107a28d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 105931566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}
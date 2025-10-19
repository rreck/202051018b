```json
{
  "id": "b30a8f4c82b0162d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292272,
  "host_pid": "9e6742732c60:1",
  "hash": "66c722065618a4a7c2f69bb9b6f56c9d938fb22bcafcefba3451f632dde817c6",
  "cid": "QmV166c722065618a4a7c2f69bb9b6f56c9d938fb22b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292272,
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
      "evaluated_at": 1760292272
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
  "sig": "6e060d63af679007988604db519850122a60b4863ca205c301db7add2cb23dcf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 84246052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}
```json
{
  "id": "6dec64c75a47fa62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291013,
  "host_pid": "9e6742732c60:1",
  "hash": "317c42a8e54e1a5b310de01a27b4bdb4896d0080f6d56755e8fbd9f27698db58",
  "cid": "QmV1317c42a8e54e1a5b310de01a27b4bdb4896d0080",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291013,
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
      "evaluated_at": 1760291013
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
  "sig": "9f0ceb9545c4c3655d9af62eb19997d41c55f7dab839aab0ac00bd6d7f81eedc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 22576125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}
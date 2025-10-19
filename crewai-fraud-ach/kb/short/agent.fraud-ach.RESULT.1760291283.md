```json
{
  "id": "0768386074408f27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291283,
  "host_pid": "9e6742732c60:1",
  "hash": "7c731e79c9170eb00437fa45e333ffe6f78f9d322aa7e0e2439a74e9cd62169e",
  "cid": "QmV17c731e79c9170eb00437fa45e333ffe6f78f9d32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291283,
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
      "evaluated_at": 1760291283
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
  "sig": "77040628e2f60a5391a3ed37b4375173f975b352d09ce24bfc137d54f8a00ab7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 72430299, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}
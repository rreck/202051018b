```json
{
  "id": "7680e8902adfb71b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286932,
  "host_pid": "9e6742732c60:1",
  "hash": "5edc38d106e1efa711890b19e520756de01bfce0f112a0405178089dfdc3eb46",
  "cid": "QmV15edc38d106e1efa711890b19e520756de01bfce0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286932,
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
      "evaluated_at": 1760286932
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "6adf3fe38ca90cb4c3ee21863dbdd73846a1aead8a44a4a18be84947aab6bbec"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16911888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}
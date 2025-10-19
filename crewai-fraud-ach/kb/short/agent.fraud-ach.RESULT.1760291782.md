```json
{
  "id": "e1aecc0fbff58355",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291782,
  "host_pid": "9e6742732c60:1",
  "hash": "4725ebea0ed671db0b395454d647a25100c36ef8ed798d26db3063946fd4b0fb",
  "cid": "QmV14725ebea0ed671db0b395454d647a25100c36ef8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291782,
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
      "evaluated_at": 1760291782
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
  "sig": "e04cab728071dcfe5bf3109a4820d186b06a9a585444d61f323549a56fb3bf60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469691170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 18300000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '3e5e2db3f0853706'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}
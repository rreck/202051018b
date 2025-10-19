```json
{
  "id": "59fd9e75442dab9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293966,
  "host_pid": "9e6742732c60:1",
  "hash": "08c698089d96f4640efe42032fc0dd840950bc18ebe55b325883c1da3debdf64",
  "cid": "QmV108c698089d96f4640efe42032fc0dd840950bc18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293966,
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
      "evaluated_at": 1760293966
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
  "sig": "4ac18b7d885064ff8d4cf4f890457f6178d62cc0ff2d9fd7a8c9e8c67fab5416"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 102826954, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}
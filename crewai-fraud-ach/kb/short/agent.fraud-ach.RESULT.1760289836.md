```json
{
  "id": "c988238f4b9f95b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289836,
  "host_pid": "9e6742732c60:1",
  "hash": "f133014fe896cb5db961f4866b89f6c6a23fddd338ccd2b162c446a136f5cbc4",
  "cid": "QmV1f133014fe896cb5db961f4866b89f6c6a23fddd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289836,
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
      "evaluated_at": 1760289836
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
  "sig": "96941c31d6f46f098594d399ea2b92ad6a32efe0fe6d3b20bae230bfc352b470"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 49214180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}
```json
{
  "id": "c365f4ef8e601133",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289905,
  "host_pid": "9e6742732c60:1",
  "hash": "2157913390cf73350066925075b802f7afb1e246d4ee1baba5fd7bd355b22482",
  "cid": "QmV12157913390cf73350066925075b802f7afb1e246",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289905,
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
      "evaluated_at": 1760289905
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
  "sig": "7f93dc287a723c7711e90655d89d5628038e244c98175df36e355d837bc05765"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020012424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 31285848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': '53913ea58eda97e4'}}}
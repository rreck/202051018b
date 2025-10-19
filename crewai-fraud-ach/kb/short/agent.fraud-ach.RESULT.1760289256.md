```json
{
  "id": "129fde7d05887802",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289256,
  "host_pid": "9e6742732c60:1",
  "hash": "ba44687409f8b34edab79005ae0c24380302aa01a1c31e1965c43081b3dc2a51",
  "cid": "QmV1ba44687409f8b34edab79005ae0c24380302aa01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289256,
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
      "evaluated_at": 1760289256
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
  "sig": "dabb4bc35195775fb9c45feff326ecd9e445645f8a5a08c45aa81b9335d69b01"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244807015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 11800000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285764, 'matching_hash': 'e3fbbc71f2accf8f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}
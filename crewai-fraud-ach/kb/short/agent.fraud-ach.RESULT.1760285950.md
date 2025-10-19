```json
{
  "id": "03c2fecd64ea4a6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285950,
  "host_pid": "9e6742732c60:1",
  "hash": "d2ca94795e9bba1341d944837c92a870646ac300c895eed223f243c520678808",
  "cid": "QmV1d2ca94795e9bba1341d944837c92a870646ac300",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285950,
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
      "evaluated_at": 1760285950
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
  "sig": "7970762966dcfdc66f16d85616bd6852e210322c81d7520ec81bd8608ec10e93"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241561723
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}
```json
{
  "id": "1e16a78897d7e7a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287612,
  "host_pid": "9e6742732c60:1",
  "hash": "d9aa7e9af0c756502bca5e7d0042eb5e879ef396e44919622d1dab13a3d04ae0",
  "cid": "QmV1d9aa7e9af0c756502bca5e7d0042eb5e879ef396",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287612,
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
      "evaluated_at": 1760287612
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
  "sig": "ececde6e7218d8cb3ef77547542361d09a2283cebe41f697c3702755fe80e57f"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 29626608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}
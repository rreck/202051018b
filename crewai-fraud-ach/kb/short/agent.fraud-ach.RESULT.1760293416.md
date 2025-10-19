```json
{
  "id": "590ba70bcf670ba6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293416,
  "host_pid": "9e6742732c60:1",
  "hash": "1f2881fc8271a92f4ed0e8d82d2b93cfc6484b82452787cadc24e29834da19ab",
  "cid": "QmV11f2881fc8271a92f4ed0e8d82d2b93cfc6484b82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293416,
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
      "evaluated_at": 1760293416
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
  "sig": "79fbd83556a3e6e8af68c3974ab388c24190b8491c86d79aa912d914910ea45d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 27473886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}